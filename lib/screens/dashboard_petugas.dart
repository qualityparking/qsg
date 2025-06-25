import 'package:flutter/material.dart';
import 'validate_screen.dart';
import '../services/auth_service.dart';
import 'login_screen.dart';

class DashboardPetugasScreen extends StatelessWidget {
  const DashboardPetugasScreen({super.key});

  void _logout(BuildContext context) async {
    await AuthService.logout();
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(builder: (_) => const LoginScreen()),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Dashboard Petugas'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => _logout(context),
          ),
        ],
      ),
      body: Center(
        child: ElevatedButton.icon(
          icon: const Icon(Icons.search),
          label: const Text('Validasi Plat Kendaraan'),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => const ValidateScreen()),
            );
          },
        ),
      ),
    );
  }
}
