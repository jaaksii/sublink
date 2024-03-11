import request from '@/utils/request'
const SetConfig = (obj) => {
  return request.post('/set_conifg', obj)
}
const GetConfig = () => {
  return request.post('/get_conifg')
}
export {
  SetConfig,
  GetConfig
}
