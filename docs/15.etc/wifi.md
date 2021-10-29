# WiFI

## コマンドでのWiFi接続

```
sudo nmcli device wifi connect 'アクセスポイント名' password 'パスワード' ifname wlan0
```

## 割り振られたWiFiのIPアドレス確認

```
ifconfig -a
```