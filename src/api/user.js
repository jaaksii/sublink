import request from '@/utils/request'
const SetUser = (obj) => {
  return request.post('/set_user', obj)
}
export {
  SetUser
}
