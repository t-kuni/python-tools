# 画像・動画関連のスクリプト集

## 初期設定

```

```

## 動画の指定区間(秒)を切り抜き

```
python trim_video.py input.mp4 10 20
```

## 最初のフレームを画像として切り出し

```
python extract_first_frame.py input.mp4 output.png
```

## 動画のフレーム数削減

1/[第２引数の数値] 倍のフレーム数になるように間引く

```
python reduce_frames.py input_video.mp4 4
```

## 動画の幅、高さを指定して切り出し（中央を起点に・単位%）

```
python clip_video.py input.mp4 50 100
```

## 動画の幅縮小（アス比維持・単位%）

```
python resize_video.py input.mp4 640
```

## gifをmp4に変換

```
python gif_to_mp4.py input.mp4
```

## 動画からXの倍数フレームを画像として切り出す

```
python extract_frames.py example.mp4 10
```