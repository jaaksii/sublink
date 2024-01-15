<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <div>
          <span style="margin-right: 10px">订阅生成管理系统 {{ver}}</span>
          <el-button icon="el-icon-s-promotion" size="mini" @click="handleOpenUrl('https://t.me/+u6gLWF0yP5NiZWQ1')">群组
          </el-button>
          <el-button  size="mini" @click="handleOpenUrl('https://github.com/jaaksii/sublink')">
            <span class="iconfont icon-githubb"></span> 开源
          </el-button>
        </div>
      </div>
      <el-tabs v-model="activeName">
        <el-tab-pane>
          <span slot="label" class="el-icon-umbrella"> 订阅管理</span>
          <el-radio v-model="radio1" label="1" border v-if="optionList.length!==0">编辑订阅</el-radio>
          <el-radio v-model="radio1" label="2" border>创建订阅</el-radio>
          <div style="margin-bottom: 10px"></div>
          <!--        编辑订阅-->
          <div v-if="radio1==='1'">
            <div>
              <el-select v-model="optionValue" placeholder="请选择">
                <el-option
                  v-for="(item,index) in optionList"
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
              >删除订阅
              </el-button>
            </div>
            <div style="margin-bottom: 10px"></div>
            <Nodelist :list="this.NodeList" v-if="optionSub!==''" @DelSubNode="DelSubNode"></Nodelist>
            <div style="margin-bottom: 10px"></div>
            <div v-if="optionValue!=''">
<!--            <el-tag type="info" style="margin-right: 10px">-->
<!--              上面为列表区域-->
<!--            </el-tag>-->
            <el-tag type="success">
              下面为编辑区域(批量添加删除)
            </el-tag>
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
            <div style="display: flex">
            <el-tag style="margin-right: 10px">生成类型</el-tag>
            <el-select v-model="EDIT.value" placeholder="生成类型" @change="handleValue('edit')">
              <el-option
                v-for="(item,index) in EDIT.option"
                :key="index"
                :value="item"
              >
              </el-option>
            </el-select>
            <MyClash v-if="EDIT.value==='clash'" style="margin-left: 10px"></MyClash>
            </div>
            <div style="margin-bottom: 10px"></div>

            <el-input
              type="text"
              v-model="optionUrl"
              readonly
            >
              <template slot="prepend">订阅地址</template>
              <template slot="append">
                <el-button size="small" icon="el-icon-document-copy" @click="handleCopy(optionUrl)">复制</el-button>
                <el-button size="small" icon="iconfont icon-erweima" @click="handleOpenQr(optionUrl)">
                  二维码
                </el-button>
              </template>
            </el-input>
            <div style="margin-bottom: 10px"></div>
            <el-button
              round
              style="position: relative;left: 50%;transform: translate(-50%)"
              @click="handleSet"
            >修改订阅
            </el-button>
          </div>
          <!--          创建订阅-->
          <div v-else>
            <el-input
              type="text"
              placeholder="订阅名称(支持emoji)"
              v-model.trim="name"
              maxlength="20"
              show-word-limit
            />
            <div style="margin-bottom: 10px"></div>
            <el-input
              type="textarea"
              placeholder="订阅或者节点多个用回车分开,每个节点最后面带上|为备注信息"
              v-model="sub"
              rows="10"
            />
            <div style="margin-bottom: 10px"></div>
            <el-button
              round
              style="position: relative;left: 50%;transform: translate(-50%)"
              @click="handleCreate"
            >创建订阅
            </el-button>
          </div>

        </el-tab-pane>
        <el-tab-pane>
          <span slot="label"><i class="el-icon-user-solid"> 账号设置</i></span>
          <USER></USER>
        </el-tab-pane>
        <el-tab-pane>
          <span slot="label"><i class="el-icon-date"> 登录记录</i></span>
          <MyAddress></MyAddress>
        </el-tab-pane>
      </el-tabs>
      <div style="padding-bottom: 5px"></div>
    </el-card>
<!--    二维码组件-->
    <el-dialog
      title="二维码"
      :visible.sync="isQrShow"
      width="30%"
    >
      <vue-qr
        :text="QrTest"
      ></vue-qr>
    </el-dialog>
  </div>
</template>

<script>
import { GetSubs, CreateSub, DelSub, SetSub, DecodeSub } from '@/api/sub'
import USER from '@/components/user'
import MyClash from '@/components/clash'
import MyAddress from '@/components/address'
import Nodelist from '@/components/nodelist'
import VueQr from 'vue-qr'
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
      optionUrl: '',
      optionList: [],
      timer: null,
      EDIT: {
        value: 'clash',
        option: ['v2ray', 'clash']
      },
      isQrShow: false,
      QrTest: '',
      ver: process.env.VUE_APP_VER,
      NodeList: []
    }
  },
  created () {
    this.GetSubs()
  },
  watch: {
    optionValue (newValue) {
      // console.log('监视' + newValue)
      // console.log(this.list)
      this.NodeList = this.list.filter(item => item.name === newValue)
      // console.log(res)
      const list = this.NodeList.map(item => item.node + (item.remarks ? '|' + item.remarks : ''))
      // console.log(list.join('\n'))
      this.optionSub = list.join('\n')
      this.handleUrl('edit')
      // let list = []
      // list = this.list.map(item => item.node + (item.remarks ? '|' + item.remarks : ''))
      // this.optionSub = list.join('\n')
      // this.handleUrl('edit')
    }
  },
  methods: {
    async GetSubs () { // 获取全部订阅
      const res = await GetSubs()
      if (res.length === 0) {
        console.log('没有节点')
      } else {
        this.list = res
        this.optionList = Array.from(new Set(this.list.map(item => item.name)))
      }
      this.list.length > 0 ? this.radio1 = '1' : this.radio1 = '2'
    },
    async handleCreate () {
      if (this.sub === '' || this.name === '') return false
      await this.isSubAddress('create')
      clearTimeout(this.timer)
      this.timer = setTimeout(async () => {
        this.sublist = this.sub.split('\n')
        const { code, msg } = await CreateSub({
          name: this.name.trim(),
          node: this.sublist
        })
        this.$message({
          message: msg,
          type: code === 200 ? 'success' : 'warning'
        })
        if (code === 200) {
          await this.GetSubs() // 刷新全部节点
          this.radio1 = '1' // 切换到编辑订阅
          this.optionValue = this.name // 编辑订阅标题选择
          this.name = ''
          this.sub = ''
        }
      }, 1000)
    },
    async handleSet () { // 编辑订阅
      if (this.optionSub === '') return false
      await this.isSubAddress('edit')
      const res = this.list.find(item => item.name === this.optionValue)
      // console.log(res, res.node)
      const list = this.optionSub.split('\n')
      const { code, msg } = await SetSub({
        name: this.optionValue.trim(),
        node: res.node,
        newNode: list
      })
      this.$message({
        message: msg,
        type: code === 200 ? 'success' : 'warning'
      })
      if (code === 200) {
        console.log('修改成功')
        this.GetSubs() // 刷新全部节点
      }
    },
    handleOpenUrl (url) {
      window.open(url)
    },
    handleOpenQr (url) { // 打开二维码展示
      this.isQrShow = true
      this.QrTest = url
      // window.open(url)
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
            this.optionList = this.optionList.filter(item => item !== this.optionValue)
            this.optionValue = '' // 更新选项值为空字符串
          }
          this.$message({
            type: code === 200 ? 'success' : 'warning',
            message: msg
          })
          if (this.optionList.length === 0) this.radio1 = '2'
        }).catch(() => {

        })
      }, 100)
    },
    handleCopy (value) {
      this.$copyText(value)
      this.$message({
        type: 'success',
        message: '复制成功'
      })
    },
    handleUrl (value) {
      if (value === 'edit') {
        const encoder = new TextEncoder()
        const byteText = encoder.encode(this.optionValue)
        const base64Value = encodeURIComponent(btoa(String.fromCharCode.apply(null, byteText)))
        // console.log(base64Value)
        this.optionUrl = location.origin + `/sub/${this.EDIT.value}/${base64Value}`
      }
    },
    async isSubAddress (index) { // 判断是否订阅地址
      // 原始字符串
      let str
      if (index === 'create') {
        str = this.sub
      } else {
        str = this.optionSub
      }
      // 使用正则表达式匹配HTTP和HTTPS网址
      const regex = /(http|https):\/\/[^\s]+/g
      const matches = str.match(regex)
      // 输出匹配的网址
      // console.log(matches)
      if (matches === null) return false
      const { code, msg } = await DecodeSub({ urls: matches })
      if (code === 200) {
        // 替换匹配的网址
        const list = msg
        if (index === 'create') {
          for (let i = 0; i <= (list.length - 1); i++) {
            this.sub = this.sub.replace(matches[i], msg[i])
          }
        } else {
          for (let i = 0; i <= (list.length - 1); i++) {
            this.optionSub = this.optionSub.replace(matches[i], msg[i] + ' ')
          }
        }
      }
      if (code === 400) {
        alert(msg)
      }
    },
    DelSubNode (id) {
      this.list = this.list.filter(item => item.id !== id)
      this.optionValue = '' // 更新选项值为空字符串
    }
  },
  components: {
    USER,
    MyClash,
    MyAddress,
    Nodelist,
    VueQr
  }
}
</script>

<style scoped>
@import "@/assets/icon/iconfont.css";
</style>
