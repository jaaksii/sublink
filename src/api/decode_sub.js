import request from '@/utils/request'
const decode_sub = (obj) => {
  return request.post('/decode_sub', obj)
}
export {
  decode_sub
}
