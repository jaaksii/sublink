import request from '@/utils/request'
const GetClash = (obj) => {
  return request.post('/clash_config', obj)
}
const GetSurge = (obj) => {
  return request.post('/surge_config', obj)
}
export {
  GetClash,
  GetSurge
}
