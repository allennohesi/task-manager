import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
})

export const taskService = {
  async getAllTasks() {
    try {
      const response = await api.get('/tasks/')
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch tasks')
    }
  },

  async getTask(id) {
    try {
      const response = await api.get(`/tasks/${id}/`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch task')
    }
  },

  async createTask(task) {
    try {
      const response = await api.post('/tasks/', task)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to create task')
    }
  },

  async updateTask(id, task) {
    try {
      // PUT for full update (title & description only)
      const response = await api.put(`/tasks/${id}/`, {
        title: task.title,
        description: task.description || '',
      })
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to update task')
    }
  },

  async toggleCompleted(id) {
    try {
      // PATCH to toggle completed status
      const response = await api.patch(`/tasks/${id}/`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to toggle task status')
    }
  },

  async deleteTask(id) {
    try {
      await api.delete(`/tasks/${id}/`)
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to delete task')
    }
  },
}

