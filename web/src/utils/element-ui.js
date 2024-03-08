import Vue from 'vue'
import {
  Button,
  Select,
  option,
  Card,
  input,
  Tabs,
  TabPane,
  radio,
  MessageBox,
  Message,
  descriptions,
  descriptionsItem,
  Icon,
  tag,
  dialog,
  badge,
  Table,
  TableColumn,
  Pagination,
  Collapse,
  CollapseItem
} from 'element-ui'
Vue.use(Button)
Vue.use(Select)
Vue.use(option)
Vue.use(Card)
Vue.use(input)
Vue.use(Tabs)
Vue.use(TabPane)
Vue.use(radio)
Vue.use(descriptions)
Vue.use(descriptionsItem)
Vue.component(MessageBox)
Vue.component(Message)
Vue.use(Icon)
Vue.use(tag)
Vue.use(dialog)
Vue.use(badge)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Pagination)
Vue.use(Collapse)
Vue.use(CollapseItem)
Vue.prototype.$msgbox = MessageBox
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$prompt = MessageBox.prompt
Vue.prototype.$message = Message
