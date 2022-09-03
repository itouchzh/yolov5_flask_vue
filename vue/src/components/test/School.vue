<template>
  <!-- 父传子 -->
  <student
    :schoolName="schoolName"
    @changeSchoolName="changeName"
    ref="studentRef"
  ></student>
</template>

<script lang="ts" setup>
import Student from './Student.vue'
import { ref,onMounted } from 'vue'
const schoolName = ref('xxx')
// 子传父，然后父再传给子
const changeName = (params:string): void => {
  console.log(params);
  
  schoolName.value = 'good'
}
const studentRef = ref()
// 使用子组件的属性
onMounted(()=>{
  console.log(studentRef.value.studentName)
  console.log(studentRef.value.obj)
})
</script>

<style></style>
