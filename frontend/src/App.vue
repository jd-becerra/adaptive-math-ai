<template>
  <main>
    <nav>
      <router-link to="/">Dashboard</router-link>
      |
      <router-link to="/student">Student</router-link>
      |
      <router-link to="/teacher">Teacher</router-link>
    </nav>
    <router-view />
  </main>
</template>
