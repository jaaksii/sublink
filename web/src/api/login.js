import request from '@/utils/request'
const login = (obj) => {
  return request.post('/login', obj)
}
export {
  login
}
