## distpicker(中国/省市区/三级联动/地址选择器) 

### 使用方法

1.导入js

```html
<script src="js/jquery.js"></script>
<script src="js/distpicker.js"></script>
```

2.给div设置 data-toggle="distpicker"

```html
<div data-toggle="distpicker">
  <select></select>
  <select></select>
  <select></select>
</div>
```

3.自定义placeholders 

```html
<div data-toggle="distpicker">
  <select data-province="---- 选择省 ----"></select>
  <select data-city="---- 选择市 ----"></select>
  <select data-district="---- 选择区 ----"></select>
</div>
```

4.自定义初始显示地区

```html
<div data-toggle="distpicker">
  <select data-province="浙江省"></select>
  <select data-city="杭州市"></select>
  <select data-district="西湖区"></select>
</div>
```

4.js回调初始化div

```javascript
$('#target').distpicker()
<div id="target">
    <select></select>
    <select></select>
    <select></select>
</div>
```

5.js回调初始化div自定义placeholders 

```javascript
$('#target').distpicker({
  province: '---- 所在省 ----',
  city: '---- 所在市 ----',
  district: '---- 所在区 ----'
})
<div id="target">
    <select></select>
    <select></select>
    <select></select>
</div>
```

6.js回调初始化div自定义默认显示地区

```javascript
$('#target').distpicker({
    province: '浙江省',
    city: '杭州市',
    district: '上城区'
})
<div id="target">
    <select></select>
    <select></select>
    <select></select>
</div>
```

7.通过div-attr设置

```html
<div data-toggle="distpicker" data-autoselect="3" data-province="浙江省">
    <select></select>
    <select></select>
    <select></select>
</div>
```

8.只显示2个/1个

```html
<div data-toggle="distpicker">
    <select></select>
    <select></select>
</div>

<div data-toggle="distpicker">
  <select></select>
</div>
```

9.默认显示(省/市/地区)

```html
// 只显示省
<div data-toggle="distpicker" data-autoselect="1">
    <select></select>
    <select></select>
    <select></select>
</div>
// 显示省和市
<div data-toggle="distpicker" data-autoselect="2">
  <select></select>
  <select></select>
  <select></select>
</div>
// 都显示
<div data-toggle="distpicker" data-autoselect="3">
  <select></select>
  <select></select>
  <select></select>
</div>
```

10.关闭placeholder

```html
<div data-toggle="distpicker" data-placeholder="false">
    <select></select>
    <select></select>
    <select></select>
</div>
```

11.通过地区邮编自定义默认地区显示

```html
<div data-toggle="distpicker" data-value-type="code">
    <select data-province="330000"></select>
    <select data-city="330100"></select>
    <select data-district="330106"></select>
</div>
```