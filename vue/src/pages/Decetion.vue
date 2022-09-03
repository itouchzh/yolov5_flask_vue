<template>
  <el-card>
    <el-upload
      ref="uploadRef"
      class="upload-demo"
      action="#"
      :auto-upload="false"
    >
      <template #trigger>
        <el-button type="primary">选择文件</el-button>
      </template>
    </el-upload>
    <div class="main-card">
      <div class="sourceImage">
        <img v-if="imgUrl" :src="imgUrl" alt="" />
      </div>
      <div class="sourceImage">
        <!-- <template #file="{file}">
            <img :src="file.url" alt="">
          </template> -->
        <img v-if="resultUrl" :src="resultUrl" alt="" />
      </div>
    </div>
    <el-button type="primary" @click="getData()">检测</el-button>
    <el-table :data="tableData" stripe style="width: 100%">
      <el-table-column prop="name" label="Name" width="180" />
      <el-table-column prop="age" label="Age" width="180" />
    </el-table>

    <el-upload
      action="#"
      list-type="picture-card"
      :auto-upload="false"
      :on-change="handleSuccess"
    >
      <el-icon><Plus /></el-icon>
      <template #file="{ file }">
        <div>
          <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
          <span class="el-upload-list__item-actions">
            <span
              class="el-upload-list__item-preview"
              @click="handlePictureCardPreview(file)"
            >
              <el-icon><zoom-in /></el-icon>
            </span>
            <span
              v-if="!disabled"
              class="el-upload-list__item-delete"
              @click="handleDownload(file)"
            >
              <el-icon><Download /></el-icon>
            </span>
            <span
              v-if="!disabled"
              class="el-upload-list__item-delete"
              @click="handleRemove(file)"
            >
              <el-icon><Delete /></el-icon>
            </span>
          </span>
        </div>
      </template>
    </el-upload>

    <el-dialog v-model="dialogVisible">
      <img w-full :src="dialogImageUrl" alt="Preview Image" />
    </el-dialog>
  </el-card>
</template>
<script lang="ts" setup>
import { ref, onMounted, toRaw, renderList } from 'vue'
import type { UploadInstance } from 'element-plus'
import axios from 'axios'
const tableData = ref([])
const imgUrl = ref('')
const resultUrl = ref('')

const uploadRef = ref<UploadInstance>()

onMounted(() => {
  //   getData()
})

import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
import type { UploadFile } from 'element-plus'
let image_base64 = ref('')
const handleSuccess = (file, filelist) => {
  //   file = toRaw(file)
  imgUrl.value = file.url
  //   console.log(imgUrl.value)
  console.log(file)
  var reader = new FileReader()
  reader.readAsDataURL(file.raw)
  reader.onload = () => {
    //   转换成base64的结果
    image_base64.value = reader.result
    // console.log(reader.result)
  }
  reader.onerror = function (error) {
    console.log('Error: ', error)
  }
}

const beforeUpload = (res, file: UploadFile) => {
  console.log(file)
}
const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const disabled = ref(false)

const handlePictureCardPreview = (file: UploadFile) => {
  //   console.log(file.url)
  dialogImageUrl.value = file.url!
  dialogVisible.value = true
}

const handleRemove = (file: UploadFile) => {
  console.log(file)
}

const handleDownload = (file: UploadFile) => {
  console.log(file)
}

const getData = async () => {
  console.log(1)
  const message = await axios
    .post('/api/students', {
      img: image_base64.value
    })
    .then((res) => {
      //   tableData.value = res.data
      // res.data是base64编码。再将这个转成图片。
      resultUrl.value = res.data
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style lang="less" scoped>
.main-card {
  display: flex;
  justify-content: space-around;
  .sourceImage img {
    height: 300px;
    width: 300px;
    background-color: palegoldenrod;
  }
}
</style>
