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
  Icon
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
Vue.prototype.$msgbox = MessageBox
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$prompt = MessageBox.prompt
Vue.prototype.$message = Message
