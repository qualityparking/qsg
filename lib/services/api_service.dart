static Future<Map<String, dynamic>> validatePlat(String plat) async {
  final token = await _getToken();
  final res = await http.get(
    Uri.parse('$baseUrl/validate-plat/$plat'),
    headers: {'Authorization': 'Bearer $token'},
  );
  return jsonDecode(res.body);
}

static Future<String> createPaymentToken(int amount) async {
  final token = await _getToken();
  final res = await http.post(
    Uri.parse('$baseUrl/payment/token'),
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer $token',
    },
    body: jsonEncode({
      'amount': amount,
      'description': 'Perpanjang Member',
    }),
  );

  final data = jsonDecode(res.body);
  return data['snap_url'];
}
