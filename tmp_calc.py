cum8 = 58085.8
cum7 = 50631.9
aug26 = cum8 - cum7
base8 = cum8 / 0.860
base7 = cum7 / 0.850
aug25 = base8 - base7
print('aug26=%.1f  base8=%.1f  base7=%.1f  aug25=%.1f' % (aug26, base8, base7, aug25))
print('yoy_aug=%.2f%%' % ((aug26 / aug25 - 1) * 100))
print('yoy_cum=%.2f%%' % ((cum8 / base8 - 1) * 100))
print('ibk sep-aug=%.2f oct-sep=%.2f' % ((-3.6907 + 5.0599), (-3.1556 + 3.6907)))
