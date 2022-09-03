<template>
  <el-button type="primary" @click="getData()">点我发送数据</el-button>
</template>

<script setup lang="ts">
import axios from 'axios'

const getData = async function () {
  const { data: res } = await axios.post('/api/g2/getOnsInfo?name=disease_h5')
  console.log(JSON.parse(res.data))
}
</script>

<style scoped lang="less"></style>
