import 'package:flutter/material.dart';
import 'validate_screen.dart';

class DashboardPetugasScreen extends StatelessWidget {
  const DashboardPetugasScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Dashboard Petugas')),
      body: Center(
        child: ElevatedButton.icon(
          icon: const Icon(Icons.search),
          label: const Text('Validasi Kendaraan'),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const ValidateScreen()),
            );
          },
        ),
      ),
    );
  }
}
