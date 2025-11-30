<template>
  <div class="task-item" :class="{ completed: task.completed }">
    <div class="task-content">
      <div class="task-header">
        <h3 :class="{ 'task-title-completed': task.completed }">
          {{ task.title }}
        </h3>
        <div class="task-actions">
          <button
            @click="toggleComplete"
            class="btn-icon"
            :title="task.completed ? 'Mark as incomplete' : 'Mark as completed'"
          >
            {{ task.completed ? '↩️' : '✓' }}
          </button>
          <button @click="showEditForm = true" class="btn-icon" title="Edit">
            ✏️
          </button>
          <button @click="handleDelete" class="btn-icon btn-delete" title="Delete">
            🗑️
          </button>
        </div>
      </div>
      <p v-if="task.description" class="task-description">
        {{ task.description }}
      </p>
      <div class="task-meta">
        <span class="task-date">
          Created: {{ formatDate(task.created_at) }}
        </span>
        <span v-if="task.completed" class="badge completed-badge">
          Completed
        </span>
      </div>
    </div>

    <TaskForm
      v-if="showEditForm"
      :task="task"
      @task-updated="handleUpdated"
      @cancel="showEditForm = false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Swal from 'sweetalert2'
import TaskForm from './TaskForm.vue'
import { taskService } from '../services/api'

const props = defineProps({
  task: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['task-updated', 'task-deleted', 'task-completed'])

const showEditForm = ref(false)

const toggleComplete = async () => {
  const wasCompleted = props.task.completed
  try {
    await taskService.toggleCompleted(props.task.id)
    emit('task-completed')
    Swal.fire({
      icon: 'success',
      title: 'Success!',
      text: `Task marked as ${wasCompleted ? 'incomplete' : 'completed'}`,
      timer: 1500,
      showConfirmButton: false,
      confirmButtonColor: '#3b82f6',
      background: '#ffffff',
      color: '#333333'
    })
  } catch (error) {
    console.error('Error toggling task completion:', error)
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: error.message || 'Failed to update task. Please try again.',
      confirmButtonColor: '#3b82f6',
      background: '#ffffff',
      color: '#333333'
    })
  }
}

const handleDelete = async () => {
  const result = await Swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3b82f6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!',
    background: '#ffffff',
    color: '#333333'
  })

  if (!result.isConfirmed) {
    return
  }

  try {
    await taskService.deleteTask(props.task.id)
    emit('task-deleted')
    Swal.fire({
      icon: 'success',
      title: 'Deleted!',
      text: 'Your task has been deleted.',
      timer: 1500,
      showConfirmButton: false,
      confirmButtonColor: '#3b82f6',
      background: '#ffffff',
      color: '#333333'
    })
  } catch (error) {
    console.error('Error deleting task:', error)
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: error.message || 'Failed to delete task. Please try again.',
      confirmButtonColor: '#3b82f6',
      background: '#ffffff',
      color: '#333333'
    })
  }
}

const handleUpdated = () => {
  showEditForm.value = false
  emit('task-updated')
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}
</script>

<style scoped>
.task-item {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 15px;
  transition: all 0.3s ease;
}

.task-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.task-item.completed {
  opacity: 0.7;
  background: #f0f0f0;
}

.task-content {
  width: 100%;
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 10px;
}

.task-header h3 {
  flex: 1;
  color: #333;
  font-size: 1.3rem;
  font-weight: 600;
  margin-right: 15px;
}

.task-title-completed {
  text-decoration: line-through;
  color: #999;
}

.task-actions {
  display: flex;
  gap: 8px;
}

.btn-icon {
  background: white;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 8px 12px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.btn-icon:hover {
  background: #f0f0f0;
  transform: scale(1.1);
}

.btn-delete:hover {
  background: #fee;
  border-color: #fcc;
}

.task-description {
  color: #666;
  margin: 10px 0;
  line-height: 1.6;
}

.task-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid #e9ecef;
}

.task-date {
  font-size: 0.85rem;
  color: #999;
}

.badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.completed-badge {
  background: #28a745;
  color: white;
}
</style>

