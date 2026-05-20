import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import StudentView from '../views/StudentView.vue'
import TeacherView from '../views/TeacherView.vue'

const routes = [
  { path: '/', name: 'dashboard', component: DashboardView },
  { path: '/student', name: 'student', component: StudentView },
  { path: '/teacher', name: 'teacher', component: TeacherView }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
