<template>
  <div>Hello World</div>
  <p>我的学校的名字是：{{ schoolName }}</p>
  <hr />
  <p>我的学校改名了：{{}}</p>
  <button @click="changeName">点击改名</button>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
const props = defineProps({
  schoolName: {
    type: String,
    default: 'error'
  }
})
// 事件声明
const emit = defineEmits(['changeSchoolName'])
const changeName = (): void => {
  emit('changeSchoolName','传递成功')
}

// 子组件中暴露属性，可以在父组件中通过ref来访问到
const studentName = ref('tom')
defineExpose({
  studentName,
  obj: {
    name: 'paul',
    age: 23
  }
})
</script>

<style></style>
