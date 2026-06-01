import requests
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

# ── Make.com webhook URL ──
MAKE_WEBHOOK = "https://hook.us2.make.com/xa7uddev8m89ceqd97d9iurxyquirtn7"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(".", "sitemap.xml")

@app.route("/counties/cooke-county-tx")
def cooke_county_tx():
    return render_template("counties/cooke-county-tx.html")

@app.route("/counties/grayson-county-tx")
def grayson_county_tx():
    return render_template("counties/grayson-county-tx.html")

@app.route("/counties/fannin-county-tx")
def fannin_county_tx():
    return render_template("counties/fannin-county-tx.html")

@app.route("/counties/lamar-county-tx")
def lamar_county_tx():
    return render_template("counties/lamar-county-tx.html")

@app.route("/counties/hopkins-county-tx")
def hopkins_county_tx():
    return render_template("counties/hopkins-county-tx.html")

@app.route("/counties/hunt-county-tx")
def hunt_county_tx():
    return render_template("counties/hunt-county-tx.html")

@app.route("/counties/collin-county-tx")
def collin_county_tx():
    return render_template("counties/collin-county-tx.html")

@app.route("/counties/denton-county-tx")
def denton_county_tx():
    return render_template("counties/denton-county-tx.html")

@app.route("/counties/wise-county-tx")
def wise_county_tx():
    return render_template("counties/wise-county-tx.html")

@app.route("/counties/jack-county-tx")
def jack_county_tx():
    return render_template("counties/jack-county-tx.html")

@app.route("/counties/parker-county-tx")
def parker_county_tx():
    return render_template("counties/parker-county-tx.html")

@app.route("/counties/tarrant-county-tx")
def tarrant_county_tx():
    return render_template("counties/tarrant-county-tx.html")

@app.route("/counties/dallas-county-tx")
def dallas_county_tx():
    return render_template("counties/dallas-county-tx.html")

@app.route("/counties/rockwall-county-tx")
def rockwall_county_tx():
    return render_template("counties/rockwall-county-tx.html")

@app.route("/counties/kaufman-county-tx")
def kaufman_county_tx():
    return render_template("counties/kaufman-county-tx.html")

@app.route("/counties/gregg-county-tx")
def gregg_county_tx():
    return render_template("counties/gregg-county-tx.html")

@app.route("/counties/wood-county-tx")
def wood_county_tx():
    return render_template("counties/wood-county-tx.html")

@app.route("/counties/smith-county-tx")
def smith_county_tx():
    return render_template("counties/smith-county-tx.html")

@app.route("/counties/henderson-county-tx")
def henderson_county_tx():
    return render_template("counties/henderson-county-tx.html")

@app.route("/counties/navarro-county-tx")
def navarro_county_tx():
    return render_template("counties/navarro-county-tx.html")

@app.route("/counties/ellis-county-tx")
def ellis_county_tx():
    return render_template("counties/ellis-county-tx.html")

@app.route("/counties/hill-county-tx")
def hill_county_tx():
    return render_template("counties/hill-county-tx.html")

@app.route("/counties/johnson-county-tx")
def johnson_county_tx():
    return render_template("counties/johnson-county-tx.html")

@app.route("/counties/hood-county-tx")
def hood_county_tx():
    return render_template("counties/hood-county-tx.html")

@app.route("/counties/mclennan-county-tx")
def mclennan_county_tx():
    return render_template("counties/mclennan-county-tx.html")

@app.route("/counties/bell-county-tx")
def bell_county_tx():
    return render_template("counties/bell-county-tx.html")

@app.route("/counties/bee-county-tx")
def bee_county_tx():
    return render_template("counties/bee-county-tx.html")

@app.route("/counties/williamson-county-tx")
def williamson_county_tx():
    return render_template("counties/williamson-county-tx.html")

@app.route("/counties/orange-county-tx")
def orange_county_tx():
    return render_template("counties/orange-county-tx.html")

@app.route("/counties/jefferson-county-tx")
def jefferson_county_tx():
    return render_template("counties/jefferson-county-tx.html")

@app.route("/counties/angelina-county-tx")
def angelina_county_tx():
    return render_template("counties/angelina-county-tx.html")

@app.route("/counties/victoria-county-tx")
def victoria_county_tx():
    return render_template("counties/victoria-county-tx.html")

@app.route("/counties/bexar-county-tx")
def bexar_county_tx():
    return render_template("counties/bexar-county-tx.html")

@app.route("/counties/harris-county-tx")
def harris_county_tx():
    return render_template("counties/harris-county-tx.html")

@app.route("/counties/comal-county-tx")
def comal_county_tx():
    return render_template("counties/comal-county-tx.html")

@app.route("/counties/dawson-county-ga")
def dawson_county_ga():
    return render_template("counties/dawson-county-ga.html")

@app.route("/counties/floyd-county-ga")
def floyd_county_ga():
    return render_template("counties/floyd-county-ga.html")

@app.route("/counties/bartow-county-ga")
def bartow_county_ga():
    return render_template("counties/bartow-county-ga.html")

@app.route("/counties/cherokee-county-ga")
def cherokee_county_ga():
    return render_template("counties/cherokee-county-ga.html")

@app.route("/counties/forsyth-county-ga")
def forsyth_county_ga():
    return render_template("counties/forsyth-county-ga.html")

@app.route("/counties/hall-county-ga")
def hall_county_ga():
    return render_template("counties/hall-county-ga.html")

@app.route("/counties/jackson-county-ga")
def jackson_county_ga():
    return render_template("counties/jackson-county-ga.html")

@app.route("/counties/barrow-county-ga")
def barrow_county_ga():
    return render_template("counties/barrow-county-ga.html")

@app.route("/counties/gwinnett-county-ga")
def gwinnett_county_ga():
    return render_template("counties/gwinnett-county-ga.html")

@app.route("/counties/dekalb-county-ga")
def dekalb_county_ga():
    return render_template("counties/dekalb-county-ga.html")

@app.route("/counties/cobb-county-ga")
def cobb_county_ga():
    return render_template("counties/cobb-county-ga.html")

@app.route("/counties/fulton-county-ga")
def fulton_county_ga():
    return render_template("counties/fulton-county-ga.html")

@app.route("/counties/douglas-county-ga")
def douglas_county_ga():
    return render_template("counties/douglas-county-ga.html")

@app.route("/counties/polk-county-ga")
def polk_county_ga():
    return render_template("counties/polk-county-ga.html")

@app.route("/counties/paulding-county-ga")
def paulding_county_ga():
    return render_template("counties/paulding-county-ga.html")

@app.route("/counties/carroll-county-ga")
def carroll_county_ga():
    return render_template("counties/carroll-county-ga.html")

@app.route("/counties/clayton-county-ga")
def clayton_county_ga():
    return render_template("counties/clayton-county-ga.html")

@app.route("/counties/rockdale-county-ga")
def rockdale_county_ga():
    return render_template("counties/rockdale-county-ga.html")

@app.route("/counties/walton-county-ga")
def walton_county_ga():
    return render_template("counties/walton-county-ga.html")

@app.route("/counties/fayette-county-ga")
def fayette_county_ga():
    return render_template("counties/fayette-county-ga.html")

@app.route("/counties/coweta-county-ga")
def coweta_county_ga():
    return render_template("counties/coweta-county-ga.html")

@app.route("/counties/henry-county-ga")
def henry_county_ga():
    return render_template("counties/henry-county-ga.html")

@app.route("/counties/newton-county-ga")
def newton_county_ga():
    return render_template("counties/newton-county-ga.html")

@app.route("/counties/spalding-county-ga")
def spalding_county_ga():
    return render_template("counties/spalding-county-ga.html")

@app.route("/counties/pike-county-ga")
def pike_county_ga():
    return render_template("counties/pike-county-ga.html")

@app.route("/counties/troup-county-ga")
def troup_county_ga():
    return render_template("counties/troup-county-ga.html")

@app.route("/counties/meriwether-county-ga")
def meriwether_county_ga():
    return render_template("counties/meriwether-county-ga.html")

@app.route("/counties/lamar-county-ga")
def lamar_county_ga():
    return render_template("counties/lamar-county-ga.html")

@app.route("/counties/monroe-county-ga")
def monroe_county_ga():
    return render_template("counties/monroe-county-ga.html")

@app.route("/counties/butts-county-ga")
def butts_county_ga():
    return render_template("counties/butts-county-ga.html")

@app.route("/counties/upson-county-ga")
def upson_county_ga():
    return render_template("counties/upson-county-ga.html")

@app.route("/counties/houston-county-ga")
def houston_county_ga():
    return render_template("counties/houston-county-ga.html")

@app.route("/counties/richmond-county-ga")
def richmond_county_ga():
    return render_template("counties/richmond-county-ga.html")

@app.route("/counties/emanuel-county-ga")
def emanuel_county_ga():
    return render_template("counties/emanuel-county-ga.html")

@app.route("/counties/liberty-county-ga")
def liberty_county_ga():
    return render_template("counties/liberty-county-ga.html")

@app.route("/blog/sell-house-fast-dallas-tx")
def blog_sell_house_fast_dallas_tx():
    return render_template("blog/sell-house-fast-dallas-tx.html")

@app.route("/blog/sell-house-fast-atlanta-ga")
def blog_sell_house_fast_atlanta_ga():
    return render_template("blog/sell-house-fast-atlanta-ga.html")

@app.route("/blog/avoid-foreclosure-texas")
def blog_avoid_foreclosure_texas():
    return render_template("blog/avoid-foreclosure-texas.html")

@app.route("/blog/selling-inherited-home-georgia")
def blog_selling_inherited_home_georgia():
    return render_template("blog/selling-inherited-home-georgia.html")

@app.route("/blog/cash-offer-vs-traditional-home-sale")
def blog_cash_offer_vs_traditional_home_sale():
    return render_template("blog/cash-offer-vs-traditional-home-sale.html")

@app.route("/blog/sell-house-as-is-dfw")
def blog_sell_house_as_is_dfw():
    return render_template("blog/sell-house-as-is-dfw.html")

@app.route("/blog/selling-house-during-divorce-texas")
def blog_selling_house_during_divorce_texas():
    return render_template("blog/selling-house-during-divorce-texas.html")

@app.route("/blog/probate-real-estate-texas-georgia")
def blog_probate_real_estate_texas_georgia():
    return render_template("blog/probate-real-estate-texas-georgia.html")

@app.route("/blog/selling-partial-interest-property")
def blog_selling_partial_interest_property():
    return render_template("blog/selling-partial-interest-property.html")

@app.route("/blog/sell-house-property-tax-delinquency")
def blog_sell_house_property_tax_delinquency():
    return render_template("blog/sell-house-property-tax-delinquency.html")

@app.route("/blog/sell-house-financial-hardship-bankruptcy")
def blog_sell_house_financial_hardship_bankruptcy():
    return render_template("blog/sell-house-financial-hardship-bankruptcy.html")

@app.route("/blog/sell-house-with-liens")
def blog_sell_house_with_liens():
    return render_template("blog/sell-house-with-liens.html")

@app.route("/blog/sell-fire-damaged-house")
def blog_sell_fire_damaged_house():
    return render_template("blog/sell-fire-damaged-house.html")

@app.route("/blog/sell-house-code-violations")
def blog_sell_house_code_violations():
    return render_template("blog/sell-house-code-violations.html")

@app.route("/blog/sell-house-problem-tenants-landlord")
def blog_sell_house_problem_tenants_landlord():
    return render_template("blog/sell-house-problem-tenants-landlord.html")

@app.route("/submit", methods=["POST"])
def submit():
    data     = request.get_json()
    honeypot = data.get("website", "").strip()
    if honeypot:
        return jsonify({"success": False, "message": "Invalid submission."}), 400
    name    = data.get("name", "").strip()
    phone   = data.get("phone", "").strip()
    address = data.get("address", "").strip()
    email   = data.get("email", "").strip()

    if not all([name, phone, address, email]):
        return jsonify({"success": False, "message": "All fields are required."}), 400

    try:
        requests.post(MAKE_WEBHOOK, json={
            "name":    name,
            "phone":   phone,
            "address": address,
            "email":   email
        })
    except Exception as e:
        print(f"Make.com error: {e}")

    return jsonify({"success": True, "message": "Thanks! We'll be in touch within 24 hours."})

if __name__ == "__main__":
    app.run(debug=True)
