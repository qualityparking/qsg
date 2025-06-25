static Future<Map<String, dynamic>> validatePlat(String plat) async {
  final token = await _getToken();
  final res = await http.get(
    Uri.parse('$baseUrl/validate-plat/$plat'),
    headers: {'Authorization': 'Bearer $token'},
  );
  return jsonDecode(res.body);
}
