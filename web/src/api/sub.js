import request from '@/utils/request'
const GetSubs = () => { // 获取全部节点
  return request.post('/get_subs')
}
const CreateSub = (obj) => { // 新建订阅
  return request.post('/create_sub', obj)
}
const CreateNode = (obj) => { // 新建节点
  return request.post('/create_node', obj)
}
const GetSubName = (name) => { // 查看指定订阅节点
  return request.post('/get_sub/' + name)
}
const DelSub = (name) => { // 删除指定订阅
  return request.post('/del_sub/' + name)
}
const DelSubNode = (id) => { // 删除指定节点
  return request.post('/del_sub_node/' + id)
}
const SetSub = (obj) => { // 批量设置订阅节点
  return request.post('/set_sub', obj)
}
const DecodeSub = (obj) => {
  return request.post('/decode_sub', obj)
}
const RenameSub = (name, obj) => {
  return request.post(`/rename_sub/${name}`, obj)
}
const SetNode = (obj) => { // 修改单个节点
  return request.post('/set_node', obj)
}
export {
  GetSubs,
  CreateSub,
  CreateNode,
  GetSubName,
  DelSub,
  DelSubNode,
  SetSub,
  DecodeSub,
  RenameSub,
  SetNode
}
