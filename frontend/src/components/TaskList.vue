<template>
  <div class="task-list">
    <div v-if="loading" class="loading">Loading tasks...</div>
    <div v-else-if="tasks.length === 0" class="empty-state">
      <p>No tasks yet. Create your first task!</p>
    </div>
    <div v-else>
      <TaskItem
        v-for="task in tasks"
        :key="task.id"
        :task="task"
        @task-updated="$emit('task-updated')"
        @task-deleted="$emit('task-deleted')"
        @task-completed="$emit('task-completed')"
      />
    </div>
  </div>
</template>

<script setup>
import TaskItem from './TaskItem.vue'

defineProps({
  tasks: {
    type: Array,
    required: true,
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

defineEmits(['task-updated', 'task-deleted', 'task-completed'])
</script>

<style scoped>
.task-list {
  margin-top: 20px;
}

.loading {
  text-align: center;
  padding: 40px;
  color: #666;
  font-size: 1.1rem;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #999;
  font-size: 1.1rem;
}
</style>

