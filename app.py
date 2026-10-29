from flask import Flask,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    receipt=""


    if request.method == "POST":
        customer_name = request.form.get("customer_name","")
        print("ALL FORM VALUES:",request.form.to_dict())
        computer_number=request.form.get("computer_number","NOT FOUND")
        pc_type = request.form.get("pc_type","standard") 
        hours_text = request.form.get("hours","0")
        hours=float(hours_text or 0) 

        if hours <= 0:
         return "Hours must be greater than zero. Go back and try again."

        if pc_type == "standard":
           rate = 50
        else:
            rate = 100

        subtotal = hours * rate

        if hours >= 5:
           discount = subtotal * 0.10
        else:
            discount = 0

        total = subtotal - discount

        receipt = f"""
        <h2>Customer Receipt</h2>
        <p>Customer name:{customer_name}</p>
        <p>Computer number:{computer_number}</p>
        <p>Computer type:{pc_type.title()}</p>
        <P>Hours used:{hours:g}</p>
        <p>Rate per hour:Ksh{rate}</P>
        <p>Subtotal:Ksh{subtotal:.2f}</p>
        <p>Discount:Ksh{discount:.2f}</p>
        <h3>Total:Ksh{total:.2f}</h3>
        """
    return f"""
    <h1>Cyber Cafe Billing System</h1>
    <form method = "POST">
    <label>Customer name:</label>
    <input name = "customer_name" required>
    <br><br>

    <label>Computer_number:</label>
    <input type = "text" name = "computer_number" required>
    <br><br>

    <label>Computer type:</label>
    <select name = "pc_type" >
    <option value = "standard" > Standard Pc</option>
    <option value = "gaming" > Gaming Pc</option>
    </select>
    <br><br>

    <label>Hours used:</label>
    <input type = "number" name= "hours"
    min = "0.1" step= "0.1" required>
    <br><br>

    <button type = "submit" > Calculate Bill</button>
 </form>
    {receipt}
    """

    if __name__ == "__main__":
       app.run()
