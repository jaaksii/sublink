<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <div>
          <span style="margin-right: 10px">订阅生成管理系统 {{ ver }}</span>
          <el-button icon="el-icon-s-promotion" size="mini" @click="handleOpenUrl('https://t.me/+u6gLWF0yP5NiZWQ1')">群组
          </el-button>
          <el-button size="mini" @click="handleOpenUrl('https://github.com/jaaksii/sublink')">
            <span class="iconfont icon-githubb"></span> 开源
          </el-button>
        </div>
      </div>
      <el-tabs v-model="activeName">
        <el-tab-pane>
          <span slot="label" class="el-icon-umbrella"> 订阅管理</span>
          <el-radio v-model="radio1" label="1" border v-if="optionList.length !== 0">编辑订阅</el-radio>
          <el-radio v-model="radio1" label="2" border>创建订阅</el-radio>
          <el-radio v-model="radio1" label="3" border>订阅解析</el-radio>
          <el-radio v-model="radio1" label="4" border>全局设置</el-radio>
          <div style="margin-bottom: 10px"></div>
          <!--        编辑订阅-->
          <div v-if="radio1 === '1'">
            <div style="display: flex">
              <el-select v-model="optionValue" placeholder="请选择">
                <el-option v-for="(item, index) in optionList" :key="index" :value="item">
                </el-option>
              </el-select>

              <rename @handleRename="handleRename" @handleDel="handleDel"></rename>
              <!--    新增节点按钮-->
              <div v-if="optionSub !== ''">
                <el-button @click="NewNode.dialogVisible = true" round type="primary" size="mini">新增节点</el-button>
                <el-dialog title="新增一个节点" :visible.sync="NewNode.dialogVisible">
                  <el-input v-model.trim="NewNode.node" type="textarea" rows="10" placeholder="节点" />
                  <div style="margin-bottom: 10px"></div>

                  <el-input v-model.trim="NewNode.remarks" placeholder="备注" @keyup.enter.native="handleNewNode" />
                  <span slot="footer" class="dialog-footer">
                    <el-button @click="NewNode.dialogVisible = false">取 消</el-button>
                    <el-button type="primary" @click="handleNewNode">确 定</el-button>
                  </span>
                </el-dialog>
              </div>
            </div>
            <div style="margin-bottom: 10px"></div>
            <Nodelist :list="this.NodeList" v-if="optionSub !== ''" @RefreshSub="RefreshSub" @CopySubNode="CopySubNode">
            </Nodelist>
            <div style="margin-bottom: 10px"></div>
            <div v-if="optionValue != ''">
              <!--            <el-tag type="info" style="margin-right: 10px">-->
              <!--              上面为列表区域-->
              <!--            </el-tag>-->
              <el-collapse accordion>
                <el-collapse-item>
                  <template slot="title">
                    <el-tag type="success">
                      展开批量编辑区域(批量添加删除)
                    </el-tag>
                  </template>
                  <div style="margin-bottom: 10px"></div>
                  <el-input type="textarea" placeholder="节点多个用回车分开,每个节点最后面带上|为备注信息" v-model="optionSub" rows="10"
                    show-word-limit />
                  <div style="margin-bottom: 10px"></div>
                  <el-button round @click="handleSet"
                    style="position: relative;left: 50%;transform: translate(-50%)">修改订阅
                  </el-button>
                </el-collapse-item>
              </el-collapse>

            </div>

            <div style="margin-bottom: 10px"></div>
            <div style="display: flex" v-if="optionSub !== ''">
              <el-tag style="margin-right: 10px">生成类型</el-tag>
              <el-select v-model="EDIT.value" placeholder="生成类型" @change="handleUrl('edit')">
                <el-option v-for="(item, index) in EDIT.option" :key="index" :value="item">
                </el-option>
              </el-select>
              <MyClash v-if="EDIT.value === 'clash'" style="margin-left: 10px"></MyClash>
              <MySurge v-if="EDIT.value === 'surge'" style="margin-left: 10px"></MySurge>
            </div>
            <div style="margin-bottom: 10px"></div>
            <div v-if="optionSub !== ''">
              <el-input type="text" v-model="optionUrl" readonly>
                <template slot="prepend">订阅地址</template>
                <template slot="append">
                  <el-button size="small" icon="el-icon-document-copy" @click="handleCopy(optionUrl)">复制</el-button>
                  <el-button size="small" icon="iconfont icon-erweima" @click="handleOpenQr(optionUrl)">
                    二维码
                  </el-button>
                </template>
              </el-input>
            </div>
          </div>
          <!--          创建订阅-->
          <div v-if="radio1 === '2'">
            <el-input type="text" placeholder="订阅名称(支持emoji)" v-model.trim="name" maxlength="20" show-word-limit />
            <div style="margin-bottom: 10px"></div>
            <el-input type="textarea" placeholder="订阅或者节点多个用回车分开,每个节点最后面带上|为备注信息" v-model="sub" rows="10" />
            <div style="margin-bottom: 10px"></div>
            <el-button round style="position: relative;left: 50%;transform: translate(-50%)" @click="handleCreate">创建订阅
            </el-button>
          </div>
          <div v-if="radio1 === '3'">
            <MyParser></MyParser>
          </div>
          <div v-if="radio1 === '4'" @change="handleConfig">
            <el-checkbox v-model="Config.udp">udp</el-checkbox>
            <el-checkbox v-model="Config.skipCert">跳过证书</el-checkbox>
            <el-checkbox v-model="Config.emoji">emoji入口国旗</el-checkbox>
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
    <el-dialog title="二维码" :visible.sync="isQrShow" width="30%">
      <vue-qr :text="QrTest"></vue-qr>
    </el-dialog>
  </div>
</template>

<script>
import { GetSubs, CreateSub, DelSub, SetSub, RenameSub, CreateNode } from '@/api/sub'
import { SetConfig, GetConfig } from '@/api/config'
import USER from '@/components/user'
import MyClash from '@/components/clash'
import MySurge from '@/components/surge'
import MyAddress from '@/components/address'
import Nodelist from '@/components/nodelist'
import Rename from '@/components/rename'
import MyParser from '@/components/parser'
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
        option: ['v2ray', 'clash', 'surge']
      },
      isQrShow: false,
      QrTest: '',
      ver: process.env.VUE_APP_VER,
      NodeList: [],
      NewNode: {
        dialogVisible: false,
        remarks: '',
        node: ''
      },
      Config: {
        udp: false,
        skipCert: false,
        emoji: false
      }
    }
  },
  created () {
    this.GetSubs()
    this.GetConfig()
  },
  watch: {
    optionValue (newValue) {
      // console.log('监视' + newValue)
      // console.log(this.list)
      this.NodeList = this.list.filter(item => item.name === newValue)
      // console.log(res)
      const list = this.NodeList.map(item => item.node + (item.remarks ? '|' + item.remarks : ''))
      // console.log(list.join('\n'))
      this.optionValue = newValue
      this.optionSub = list.join('\n')
      this.handleUrl('edit')
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
        this.NodeList = this.list.filter(item => item.name === this.optionValue)
        const NodeList = this.NodeList.map(item => item.node + (item.remarks ? '|' + item.remarks : ''))
        // console.log(list.join('\n'))
        this.optionSub = NodeList.join('\n')
      }
      this.list.length > 0 ? this.radio1 = '1' : this.radio1 = '2'
    },
    async handleCreate () {
      if (this.sub === '' || this.name === '') return false
      // await this.isSubAddress('create')
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
      // await this.isSubAddress('edit')
      const res = this.list.find(item => item.name === this.optionValue)
      console.log(res, res.node)
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
        // console.log('修改成功')
        // this.optionValue = ''
        this.GetSubs() // 刷新全部节点
        // console.log(this.NodeList)
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
    CopySubNode (text) {
      this.handleCopy(text)
    },
    RefreshSub () {
      this.GetSubs()
    },
    async handleRename (rename) {
      if (this.optionValue !== '' && rename !== '') {
        const { code, msg } = await RenameSub(this.optionValue,
          {
            newName: rename
          }
        )
        this.$message({
          message: msg,
          type: code === 200 ? 'success' : 'warning'
        })
        if (code === 200) {
          this.GetSubs()
          this.optionValue = rename // 更新当前下拉标题
        }
      }
    },
    async handleNewNode () {
      const { code, msg } = await CreateNode({
        name: this.optionValue,
        node: this.NewNode.node.trim(),
        remarks: this.NewNode.remarks.trim()
      })
      if (code === 200) {
        // console.log(code, msg)
        this.GetSubs()
        this.NewNode.dialogVisible = false
        this.NewNode.node = ''
        this.NewNode.remarks = ''
      }
      this.$message({
        type: code === 200 ? 'success' : 'warning',
        message: msg
      })
    },
    handleConfig () {
      clearTimeout(this.timer)
      this.timer = setTimeout(async () => {
        const { code, msg } = await SetConfig({
          udp: this.Config.udp,
          skipcert: this.Config.skipCert,
          emoji: this.Config.emoji
        })
        this.$message({
          type: code === 200 ? 'success' : 'warning',
          message: msg
        })
      }, 1000)
    },
    async GetConfig () {
      const { udp, skipcert, emoji } = await GetConfig()
      this.Config.udp = udp
      this.Config.skipCert = skipcert
      this.Config.emoji = emoji
    }
  },
  components: {
    USER,
    MyClash,
    MySurge,
    MyAddress,
    Nodelist,
    MyParser,
    Rename,
    VueQr
  }
}
</script>

<style scoped>
@import "@/assets/icon/iconfont.css";
</style>
