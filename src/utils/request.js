import axios from 'axios'
const baseURL = '/api'
const instance = axios.create({
  baseURL: baseURL
})
const isTokenExpired = () => {
  const token = JSON.parse(localStorage.getItem('token'))
  if (token) { // 判断是否过期
    const payload = token.split('.')[1]
    const decoded = JSON.parse(atob(payload))
    const NowTime = Math.floor(new Date() / 1000)
    return NowTime > decoded.exp
  }
}
const SetRefresh = async () => { // 刷新token
  try {
    const response = await axios.post(`${baseURL}/refresh`, {}, {
      headers: {
        Authorization: 'Bearer ' + JSON.parse(localStorage.getItem('refresh'))
      }
    })
    if (response.status === 200) {
      localStorage.setItem('token', JSON.stringify(response.data)) // 设置token
      return response.data
    }
  } catch (error) {
    console.error('刷新令牌请求失败', error)
    throw error // 抛出异常，由调用方处理
  }
}
// 添加请求拦截器
instance.interceptors.request.use(async function (config) {
  // 在发送请求之前做些什么
  if (isTokenExpired()) { // 判断过期后刷新令牌
    try {
      await SetRefresh()
      // 刷新成功后重新发起请求
    } catch (error) {
      throw new Error('Token 刷新失败')
    }
  }
  config.headers.Authorization = 'Bearer ' + JSON.parse(localStorage.getItem('token'))
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error)
})

// 添加响应拦截器
instance.interceptors.response.use(function (response) {
  // 2xx 范围内的状态码都会触发该函数。
  // 对响应数据做点什么
  return response.data
}, function (error) {
  // 超出 2xx 范围的状态码都会触发该函数。
  // 对响应错误做点什么
  return Promise.reject(error)
})
export default instance
