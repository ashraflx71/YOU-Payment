from flask import Flask, render_template, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

# تسجيل الطلبات في ملف لحفظ حقوقك وأرشيفك
def log_to_csv(data):
    with open('payments_log.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data['meter'], data['amount']])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    # هنا يتم الربط المنطقي للعملية
    log_to_csv(data)
    
    # الرد من الموقع نفسه
    return jsonify({
        "status": "تم استلام الطلب بنجاح",
        "details": f"العداد: {data['meter']} | المبلغ: {data['amount']} ج.م",
        "next_step": "يرجى تحويل المبلغ عبر إنستا باي/فودافون كاش وتأكيد العملية."
    })

if __name__ == '__main__':
    app.run(debug=True)
