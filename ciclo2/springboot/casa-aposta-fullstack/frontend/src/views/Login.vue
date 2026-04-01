<template>
<div>
<h2>Login</h2>
<input v-model="email" placeholder="Email"/>
<input v-model="password" type="password" placeholder="Senha"/>
<button @click="login">Entrar</button>
</div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const login = async () => {
  await axios.post('http://localhost:8080/auth/login', {
    email: email.value,
    password: password.value
  })
}
</script>
