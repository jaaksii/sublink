<template>
<div>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>订阅生成管理系统 Im:坤坤</span>
    </div>
    <el-tabs v-model="activeName">
      <el-tab-pane>
        <span slot="label">订阅管理</span>
        <el-radio v-model="radio1" label="1" border v-if="filteredList.length!==0">编辑订阅</el-radio>
        <el-radio v-model="radio1" label="2" border>创建订阅</el-radio>
        <div style="margin-bottom: 10px"></div>
<!--        编辑订阅-->
        <div v-if="radio1==='1'">
          <div>
          <el-select v-model="optionValue" placeholder="请选择">
            <el-option
              v-for="(item,index) in filteredList"
              :key="index"
              :value="item">
            </el-option>
          </el-select>
            <el-button
              type="danger"
              size="mini"
              style="margin-left: 10px"
              @click="handleDel"
              round
            >删除订阅</el-button>
          </div>
          <div style="margin-bottom: 10px"></div>
          <el-input
            type="textarea"
            placeholder="节点多个用回车分开,每个节点最后面带上|为备注信息"
            v-model="optionSub"
            rows="10"
            show-word-limit
          />
          <div style="margin-bottom: 10px"></div>
          <el-button
            round
            style="position: relative;left: 50%;transform: translate(-50%)"
            @click="handleSet"
          >修改订阅</el-button>
        </div>
<!--          创建订阅-->
        <div v-else>
          <el-input
            type="text"
            placeholder="订阅名称"
            v-model="name"
            maxlength="20"
            show-word-limit
          />
          <div style="margin-bottom: 10px"></div>
          <el-input
            type="textarea"
            placeholder="节点多个用回车分开,每个节点最后面带上|为备注信息"
            v-model="sub"
            rows="10"
          />
          <div style="margin-bottom: 10px"></div>
          <div v-if="url!==''">
            <el-input
              type="text"
              v-model="url"
              readonly
            >
              <template slot="prepend">订阅地址</template>
              <template slot="append">
                <el-button size="small" @click="handleOpenUrl(url)">打开</el-button>
              </template>
            </el-input>
          </div>
          <div style="margin-bottom: 10px"></div>
          <el-button
            round
            style="position: relative;left: 50%;transform: translate(-50%)"
            @click="handleCreate"
          >创建订阅</el-button>
        </div>

      </el-tab-pane>
      <el-tab-pane>
        <span slot="label">账号设置</span>
        <User></User>
      </el-tab-pane>
    </el-tabs>
    <div style="padding-bottom: 5px"></div>
  </el-card>
</div>
</template>

<script>
import { GetSub, CreateSub, DelSub, SetSub } from '@/api/sub'
import User from '@/components/user'
export default {
  name: 'MyIndex',
  data () {
    return {
      activeName: '',
      name: '',
      sub: '',
      sublist: [],
      url: '',
      radio1: '2',
      list: [],
      optionValue: '',
      optionSub: '',
      filteredList: [],
      timer: null
    }
  },
  created () {
    this.GetSub()
    this.list.length > 0 ? this.radio1 = '1' : this.radio1 = '2'
  },
  watch: {
    optionValue (newValue) {
      console.log(newValue)
      const res = this.list.filter(item => item.name === newValue)
      const list = res.map(item => item.node + (item.remarks ? '|' + item.remarks : ''))
      this.optionSub = list.join('\n')
    }
  },
  methods: {
    async GetSub () { // 获取全部节点
      const res = await GetSub()
      if (res.length === 0) {
        console.log('没有节点')
      } else {
        this.list = res
        this.filteredList = Array.from(new Set(this.list.map(item => item.name)))
      }
    },
    handleCreate () {
      if (this.sub === '' || this.name === '') return false
      clearTimeout(this.timer)
      this.timer = setTimeout(async () => {
        this.sublist = this.sub.split('\n')
        const { code, msg } = await CreateSub({
          name: this.name,
          node: this.sublist
        })
        this.$message({
          message: msg,
          type: code === 200 ? 'success' : 'warning'
        })
        if (code === 200) {
          this.url = location.href + 'url/' + this.name
          this.filteredList.push(this.name)
          this.GetSub() // 刷新全部节点
          this.optionValue = '' // 更新选项值为空字符串
        }
      }, 1000)
    },
    async handleSet () {
      if (this.optionSub === '') return false
      const res = this.list.find(item => item.name === this.optionValue)
      // console.log(res, res.node)
      const list = this.optionSub.split('\n')
      const { code, msg } = await SetSub({
        name: this.optionValue,
        node: res.node,
        newNode: list
      })
      this.$message({
        message: msg,
        type: code === 200 ? 'success' : 'warning'
      })
      if (code === 200) {
        console.log('修改成功')

        // this.optionValue = this.name // 更新选项值为空字符串
      }
    },
    handleOpenUrl (url) {
      window.open(url)
    },
    handleDel () {
      clearTimeout(this.timer)
      this.timer = setTimeout(() => {
        this.$confirm('此操作将永久删除该订阅, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(async () => {
          const { code, msg } = await DelSub(this.optionValue)
          if (code === 200) {
            this.filteredList = this.filteredList.filter(item => item !== this.optionValue)
            this.optionValue = '' // 更新选项值为空字符串
          }
          this.$message({
            type: code === 200 ? 'success' : 'warning',
            message: msg
          })
          if (this.filteredList.length === 0) this.radio1 = '2'
        }).catch(() => {

        })
      }, 1000)
    }
  },
  components: {
    User
  }
}
</script>

<style scoped>

</style>
