# lcdmsg

AQM1602をI2Cで接続してメッセージを出力するプログラム

## 使い方

    lcdmsg "位置" "文字列" "位置" "文字列"

位置:
+ U == 上段
+ D == 下段

文字列: 16文字以内のANK文字

## 使用例

    lcdmsg D "192.168.0.1" U "IP ADDRESS"

## 必要なパッケージ

    PySensDevLibs

