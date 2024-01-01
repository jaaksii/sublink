import request from '@/utils/request'
const GetClash = (obj) => {
  return request.post('/clash_config', obj)
}
export {
  GetClash
}
