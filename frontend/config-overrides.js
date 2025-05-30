const { override, addBabelPlugins } = require('customize-cra');

module.exports = {
  webpack: override(
    addBabelPlugins(
      '@babel/plugin-proposal-optional-chaining',
      '@babel/plugin-proposal-nullish-coalescing-operator'
    )
  ),
  devServer: (configFunction) => {
    return (proxy, allowedHost) => {
      const config = configFunction(proxy, allowedHost);
      config.allowedHosts = ['all'];
      return config;
    };
  }
};