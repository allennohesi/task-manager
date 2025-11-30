<template>
  <div class="task-form-container">
    <form @submit.prevent="handleSubmit" class="task-form">
      <h2>{{ isEditing ? 'Edit Task' : 'Create New Task' }}</h2>
      
      <div class="form-group">
        <label for="title">Title *</label>
        <input
          id="title"
          v-model="formData.title"
          type="text"
          required
          placeholder="Enter task title"
          class="form-input"
        />
      </div>

      <div class="form-group">
        <label for="description">Description</label>
        <textarea
          id="description"
          v-model="formData.description"
          rows="4"
          placeholder="Enter task description (optional)"
          class="form-input"
        ></textarea>
      </div>


      <div class="form-actions">
        <button type="submit" class="btn btn-primary" :disabled="submitting">
          {{ submitting ? 'Saving...' : (isEditing ? 'Update Task' : 'Create Task') }}
        </button>
        <button type="button" @click="handleCancel" class="btn btn-secondary">
          Cancel
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Swal from 'sweetalert2'
import { taskService } from '../services/api'

const props = defineProps({
  task: {
    type: Object,
    default: null,
  },
})

const emit = defineEmits(['task-created', 'task-updated', 'cancel'])

const formData = ref({
  title: '',
  description: '',
  completed: false,
})

const submitting = ref(false)

const isEditing = computed(() => !!props.task)

onMounted(() => {
  if (props.task) {
    formData.value = {
      title: props.task.title,
      description: props.task.description || '',
      completed: props.task.completed,
    }
  }
})

const handleSubmit = async () => {
  submitting.value = true
  try {
    if (isEditing.value) {
      await taskService.updateTask(props.task.id, formData.value)
      emit('task-updated')
      Swal.fire({
        icon: 'success',
        title: 'Updated!',
        text: 'Task has been updated successfully.',
        timer: 1500,
        showConfirmButton: false,
        confirmButtonColor: '#3b82f6',
        background: '#ffffff',
        color: '#333333'
      })
    } else {
      await taskService.createTask(formData.value)
      emit('task-created')
      Swal.fire({
        icon: 'success',
        title: 'Created!',
        text: 'Task has been created successfully.',
        timer: 1500,
        showConfirmButton: false,
        confirmButtonColor: '#3b82f6',
        background: '#ffffff',
        color: '#333333'
      })
      // Reset form
      formData.value = {
        title: '',
        description: '',
        completed: false,
      }
    }
  } catch (error) {
    console.error('Error saving task:', error)
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: error.message || 'Failed to save task. Please try again.',
      confirmButtonColor: '#3b82f6',
      background: '#ffffff',
      color: '#333333'
    })
  } finally {
    submitting.value = false
  }
}

const handleCancel = () => {
  emit('cancel')
}
</script>

<style scoped>
.task-form-container {
  margin-bottom: 30px;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
  border: 2px dashed #dee2e6;
}

.task-form h2 {
  color: #333;
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #555;
  font-weight: 600;
  font-size: 0.9rem;
}

.form-input {
  width: 100%;
  padding: 12px;
  border: 2px solid #e9ecef;
  border-radius: 6px;
  font-size: 1rem;
  font-family: inherit;
  transition: border-color 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: #667eea;
}

textarea.form-input {
  resize: vertical;
  min-height: 100px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  font-weight: normal;
}

.checkbox {
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.form-actions {
  display: flex;
  gap: 10px;
  margin-top: 25px;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background: #5a6268;
  transform: translateY(-2px);
}
</style>

