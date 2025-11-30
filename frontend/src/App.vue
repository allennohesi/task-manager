<template>
  <div class="app">
    <div class="container">
      <header class="header">
        <h1>📋 Task Manager</h1>
        <button @click="showCreateForm = !showCreateForm" class="btn btn-primary">
          {{ showCreateForm ? 'Cancel' : '+ New Task' }}
        </button>
      </header>

      <TaskForm 
        v-if="showCreateForm" 
        @task-created="handleTaskCreated"
        @cancel="showCreateForm = false"
      />

      <TaskList 
        :tasks="tasks" 
        :loading="loading"
        @task-updated="fetchTasks"
        @task-deleted="fetchTasks"
        @task-completed="fetchTasks"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Swal from 'sweetalert2'
import TaskList from './components/TaskList.vue'
import TaskForm from './components/TaskForm.vue'
import { taskService } from './services/api'

const tasks = ref([])
const loading = ref(false)
const showCreateForm = ref(false)

const fetchTasks = async () => {
  loading.value = true
  try {
    tasks.value = await taskService.getAllTasks()
  } catch (err) {
    console.error('Error fetching tasks:', err)
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: err.message || 'Failed to load tasks. Please try again.',
      confirmButtonColor: '#3b82f6',
      background: '#ffffff',
      color: '#333333'
    })
  } finally {
    loading.value = false
  }
}

const handleTaskCreated = () => {
  showCreateForm.value = false
  fetchTasks()
}

onMounted(() => {
  fetchTasks()
})
</script>

<style scoped>
.app {
  min-height: 100vh;
}

.container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  padding: 30px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}

.header h1 {
  color: #333;
  font-size: 2rem;
  font-weight: 700;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

</style>

