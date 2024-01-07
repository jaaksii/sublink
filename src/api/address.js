import request from '@/utils/request'
const GetAddress = () => {
  return request.post('/get_ip_address')
}
export {
  GetAddress
}
