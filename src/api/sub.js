import request from '@/utils/request'
const GetSub = () => { // 获取全部节点
  return request.post('/get_subs')
}
const CreateSub = (obj) => { // 新建节点
  return request.post('/create_sub', obj)
}
const GetSubName = (name) => { // 查看指定订阅节点
  return request.post('/get_sub/' + name)
}
const DelSub = (name) => { // 删除指定订阅节点
  return request.post('/del_sub/' + name)
}
const SetSub = (obj) => { // 删除指定订阅节点
  return request.post('/set_sub', obj)
}
const DecodeSub = (obj) => {
  return request.post('/decode_sub', obj)
}
export {
  GetSub,
  CreateSub,
  GetSubName,
  DelSub,
  SetSub,
  DecodeSub
}
