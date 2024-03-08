<template>
<div>
  <div>
  <el-input
    type="textarea"
    placeholder="仅支持base64编码的订阅多条用回车区分开"
    v-model="ParserUrl"
    rows="10"
    show-word-limit
  />
</div>
  <div style="margin-bottom: 10px"></div>
  <div v-if="results">
    <el-input
      type="textarea"
      placeholder="输出结果"
      v-model="ParserList"
      rows="10"
      show-word-limit
    />
  </div>
  <div style="margin-bottom: 10px"></div>
  <el-button
    style="position: relative;left: 50%;transform: translate(-50%)"
    @click="isSubAddress2"
  >解析
  </el-button>
</div>
</template>

<script>
import { DecodeSub } from '@/api/sub'

export default {
  name: 'MyParser',
  data () {
    return {
      ParserUrl: '',
      ParserList: '',
      results: false
    }
  },
  methods: {
    async isSubAddress2 () { // 判断是否订阅地址
      // 使用正则表达式匹配HTTP和HTTPS网址
      const regex = /(http|https):\/\/[^\s]+/g
      const matches = this.ParserUrl.match(regex)
      // 输出匹配的网址
      if (matches === null) return this.$message.error('格式不正确')
      const { code, msg } = await DecodeSub({ urls: matches })
      if (code === 200) {
        this.ParserList = msg.join('\n')
        this.results = true
      }
      if (code === 400) {
        this.$message.error(msg)
      }
    }

  }
}
</script>

<style scoped>

</style>
