import pytse_client as tse
name = input("نام سهام شما چیست؟")
tse.download(symbols=name, write_to_csv=True , include_jdate=True)
ticker = tse.Ticker(name)
print(ticker.history)  # سابقه قیمت سهم
print(ticker.title)  # نام شرکت
print(ticker.url)  # آدرس صفحه سهم
print(ticker.group_name)  # نام گروه
print(ticker.eps)  # eps
print(ticker.p_e_ratio)  # P/E
print(ticker.group_p_e_ratio)  # گروهP/E
print(ticker.base_volume)  # حجم مبنا
print(ticker.last_price)  # آخرین معامله
print(ticker.adj_close)  # قیمت پایانی
print(ticker.best_supply_price)  # قیمت بهترین تقاضا
print(ticker.best_supply_vol)  # حجم بهترین تقاضا
print(ticker.best_demand_price)  # قیمت بهترین عرضه
print(ticker.best_demand_vol)  # حجم بهترین عرضه
print(ticker.shareholders)  # اطلاعات سهام داران عمده
print(ticker.client_types) #اطلاعات حقیقی و حقوقی
#date : تاریخ
#individual_buy_count : تعداد معاملات خرید حقیقی
#corporate_buy_count : تعداد معلاملات خرید حقوقی
# individual_sell_count : تعداد معاملات فروش حقیقی
# corporate_sell_count : تعداد معلاملات فروش حقوقی
# individual_buy_vol : حجم خرید حقیقی
# corporate_buy_vol : حجم خرید حقوقی
# individual_sell_vol : حجم فروش حقیقی
# corporate_sell_value : حجم فروش حقوقی
# individual_buy_mean_price : قیمت میانگین خرید حقیقی
# individual_sell_mean_price : قیمت میانگین فروش حقیقی
# corporate_buy_mean_price : قیمت میانگین خرید حقوقی
# corporate_sell_mean_price : قیمت میانگین فروش حقوقی
# individual_ownership_change : تغییر مالکیت حقوقی به حقیقی
#print(ticker.shareholders) # اطلاعات سهام داران عمده
shmshn = ticker.shareholders.percentage.sum()
shmshnsad = 100 - ticker.shareholders.percentage.sum()
print(shmshnsad) # سهم شناور
