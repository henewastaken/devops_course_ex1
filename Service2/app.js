const express = require('express');
const os = require('os');
const { execSync } = require('child_process');
const app = express();
const port = 8200;

function getIP() {
  const interfaces = os.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    for (const intf of interfaces[name]) {
      if (intf.family === 'IPv4' && !intf.internal) {
        return intf.address;
      }
    }
  }
}

function getRunningProcesses() {
  return execSync('ps -ax').toString();
}

function getFreeDiskSpace() {
  return execSync('df -h /').toString();
}

function getUptime() {
  return os.uptime();
}

app.get('/', (req, res) => {
  res.json({
    service: 'Service2',
    ip_address: getIP(),
    running_processes: getRunningProcesses(),
    free_disk_space: getFreeDiskSpace(),
    uptime: getUptime(),
  });
});

app.listen(port, () => {
  console.log(`Service2 listening at http://0.0.0.0:${port}`);
});
