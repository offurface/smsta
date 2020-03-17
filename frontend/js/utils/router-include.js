export default function(path, routes, namespace = null) {
  const parentPath = path.replace(/\//g, '')

  const newRoutes = routes.map(value => {
    if ('name' in value) {
      value.name = `${namespace}.${value.name}`
    }
    const path = value.path.replace(/\//g, '')
    if (path) {
      value.path = `/${parentPath}/${path}/`
    } else {
      value.path = `/${parentPath}/`
    }

    return value
  })

  return newRoutes
}
