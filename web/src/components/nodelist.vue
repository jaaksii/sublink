<template>
  <div>
  <el-table
    :data="list"
    border
    style="width: 100%">
    <el-table-column
      fixed
      type="index"
      label="id"
    >
    </el-table-column>
    <el-table-column
      prop="node"
      label="节点"
      show-overflow-tooltip
    >
    </el-table-column>
    <el-table-column
      prop="remarks"
      label="备注"
      width="100"
      show-overflow-tooltip
    >
    </el-table-column>
    <el-table-column
      label="操作"
      >
      <template slot-scope="scope">
        <el-button @click="handleEditPop(scope.row)" type="text" size="small">编辑</el-button>
        <el-button @click="handleCopy(scope.row)" type="text" size="small">复制</el-button>
        <el-button @click="handleDel(scope.row)" type="text" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <el-dialog
    title="单个节点编辑"
    :visible.sync="dialogVisible"
  >
    <el-input
      v-model.trim="Edit.node"
      type="textarea"
      rows="10"
      placeholder="节点"
    />
    <div style="margin-bottom: 10px"></div>

    <el-input
      v-model.trim="Edit.remarks"
      placeholder="备注"
      @keyup.enter.native="handleEdit"
    />
    <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="handleEdit">确 定</el-button>
  </span>
  </el-dialog>
  </div>
</template>

<script>
import { DelSubNode, SetNode } from '@/api/sub'
export default {
  name: 'NodeList',
  data () {
    return {
      dialogVisible: false,
      Edit: {
        id: 0,
        remarks: '',
        node: ''
      }
    }
  },
  props: {
    list: Array
  },
  created () {
    // console.log(this.list)
  },
  methods: {
    handleCopy ({ node }) {
      this.$emit('CopySubNode', node)
    },
    handleDel ({ id }) {
      console.log(id)
      this.$confirm('此操作将永久删除该节点, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: true
      }).then(async () => {
        const { code, msg } = await DelSubNode(id)
        if (code === 200) {
          this.$emit('RefreshSub')
        }
        this.$message({
          type: code === 200 ? 'success' : 'warning',
          message: msg
        })
      }).catch(() => {

      })
    },
    handleEditPop ({ id, node, remarks }) {
      this.Edit.id = id
      this.Edit.node = node
      this.Edit.remarks = remarks
      this.dialogVisible = true
    },
    async handleEdit () {
      const { code, msg } = await SetNode({
        id: this.Edit.id,
        node: this.Edit.node.trim(),
        remarks: this.Edit.remarks.trim()
      })
      if (code === 200) {
        // console.log(code, msg)
        this.$emit('RefreshSub')
        this.dialogVisible = false
      }
      this.$message({
        type: code === 200 ? 'success' : 'warning',
        message: msg
      })
    }

  }
}
</script>
