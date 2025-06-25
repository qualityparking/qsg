import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../widgets/qr_scanner.dart';

class ValidateScreen extends StatefulWidget {
  const ValidateScreen({super.key});

  @override
  State<ValidateScreen> createState() => _ValidateScreenState();
}

class _ValidateScreenState extends State<ValidateScreen> {
  final _platController = TextEditingController();
  Map<String, dynamic>? _result;

  void _validate() async {
    final result = await ApiService.validatePlat(_platController.text.trim());
    setState(() => _result = result);
  }

  void _openQRScanner() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => QRScannerScreen(
          onScanned: (code) {
            _platController.text = code;
            _validate();
          },
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Validasi Plat')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _platController,
              decoration: const InputDecoration(labelText: 'Plat Nomor'),
            ),
            const SizedBox(height: 10),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton(
                    onPressed: _validate,
                    child: const Text('Cek'),
                  ),
                ),
                const SizedBox(width: 10),
                ElevatedButton.icon(
                  icon: const Icon(Icons.qr_code_scanner),
                  label: const Text('Scan'),
                  onPressed: _openQRScanner,
                ),
              ],
            ),
            const SizedBox(height: 20),
            _result == null
                ? const Text('Belum ada hasil')
                : _result!['status'] == 'tidak ditemukan'
                    ? const Text('🚫 Tidak ditemukan')
                    : Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text("Plat: ${_result!['plat']}"),
                          Text("Status: ${_result!['status']}"),
                          if (_result!['member'] != null)
                            Text("Member aktif s/d: ${_result!['member']['berlaku_sampai']}"),
                          if (_result!['parkir'] != null)
                            Text("Masuk: ${_result!['parkir']['masuk']}"),
                        ],
                      )
          ],
        ),
      ),
    );
  }
}
