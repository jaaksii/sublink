<template>
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
      width="100">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { DelSubNode } from '@/api/sub'
export default {
  name: 'NodeList',
  data () {
    return {
    }
  },
  props: {
    list: Array
  },
  created () {
    console.log(this.list)
  },
  methods: {
    handleClick ({ id }) {
      console.log(id)
      this.$confirm('此操作将永久删除该节点, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: true
      }).then(async () => {
        const { code, msg } = await DelSubNode(id)
        if (code === 200) {
          this.$emit('DelSubNode', id)
        }
        this.$message({
          type: code === 200 ? 'success' : 'warning',
          message: msg
        })
      }).catch(() => {

      })
    }

  }
}
</script>
