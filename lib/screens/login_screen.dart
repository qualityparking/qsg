import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';
import 'dashboard_member.dart';
import 'dashboard_petugas.dart';
import 'register_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();
  bool loading = false;

  void _login() async {
    setState(() => loading = true);
    final result = await ApiService.login(usernameController.text, passwordController.text);
    setState(() => loading = false);

    if (result != null && result['token'] != null) {
      await AuthService.saveAuth(result['token'], result['role']);
      if (result['role'] == 'petugas') {
        Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const DashboardPetugasScreen()));
      } else {
        Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const DashboardMemberScreen()));
      }
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Login gagal')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Login')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: usernameController, decoration: const InputDecoration(labelText: 'Username')),
            TextField(controller: passwordController, obscureText: true, decoration: const InputDecoration(labelText: 'Password')),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: loading ? null : _login,
              child: loading ? const CircularProgressIndicator() : const Text('Login'),
            ),
            TextButton(
              onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const RegisterScreen())),
              child: const Text('Daftar akun'),
            )
          ],
        ),
      ),
    );
  }
}
