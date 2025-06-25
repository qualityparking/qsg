import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';
import '../services/api_service.dart';

class PaymentScreen extends StatefulWidget {
  final int amount;
  const PaymentScreen({super.key, required this.amount});

  @override
  State<PaymentScreen> createState() => _PaymentScreenState();
}

class _PaymentScreenState extends State<PaymentScreen> {
  String snapUrl = '';

  @override
  void initState() {
    super.initState();
    _initiatePayment();
  }

  void _initiatePayment() async {
    final url = await ApiService.createPaymentToken(widget.amount);
    setState(() => snapUrl = url);
  }

  @override
  Widget build(BuildContext context) {
    if (snapUrl.isEmpty) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    return Scaffold(
      appBar: AppBar(title: const Text('Pembayaran QRIS')),
      body: WebView(
        initialUrl: snapUrl,
        javascriptMode: JavascriptMode.unrestricted,
        onPageFinished: (url) {
          if (url.contains('finish')) {
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(content: Text('Pembayaran selesai!')),
            );
            Navigator.pop(context);
          }
        },
      ),
    );
  }
}
