<template>
<div>
  <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      fixed
      type="index"
      label="id">
    </el-table-column>
    <el-table-column
      prop="ip"
      label="ip地址">
    </el-table-column>
    <el-table-column
      prop="address"
      label="来源">
    </el-table-column>
    <el-table-column
      prop="time"
      label="时间"
      sortable
    >
    </el-table-column>
  </el-table>
  <el-pagination
    background
    layout="total, sizes, prev, pager, next, jumper"
    :current-page="tablePage.pageNum"
    :page-size="tablePage.pageSize"
    :page-sizes="pageSizes"
    :total="tablePage.total"
    @size-change="handleSizeChange"
    @current-change="handlePageChange"
    v-if="isPageShow"
  />
</div>
</template>

<script>
import { GetAddress } from '@/api/address'
export default {
  name: 'MyAddress',
  data () {
    return {
      tableDataAll: [],
      tableData: [],
      tablePage: {
        pageNum: 1, // 第几页
        pageSize: 20, // 每页多少条
        total: 0 // 总记录数
      },
      pageSizes: [10, 20, 30],
      isPageShow: true
    }
  },
  created () {
    this.get_ip_address()
  },
  methods: {
    async get_ip_address () {
      const res = await GetAddress()
      this.tableDataAll = res
      this.handleGetList()
    },
    handleGetList () { // 解析数据
      this.tableData = this.tableDataAll.slice(
        (this.tablePage.pageNum - 1) * this.tablePage.pageSize
        , this.tablePage.pageNum * this.tablePage.pageSize
      ) // 截取数组
      this.tablePage.total = this.tableDataAll.length
    },
    handlePageChange (currentPage) { // 单击分页按钮事件
      this.tablePage.pageNum = currentPage
      this.handleGetList()
      // 在此刷新数据
    },
    handleSizeChange (pageSize) { // 单击分页显示数目
      this.tablePage.pageSize = pageSize
      this.handleGetList()
      // 在此刷新数据
    }
  }
}
</script>

<style scoped>

</style>
