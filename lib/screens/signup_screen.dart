import 'package:flutter/material.dart';

class SignupScreen extends StatefulWidget {
  const SignupScreen({super.key});

  @override
  State<SignupScreen> createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  bool _termsAccepted = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF1E1E1E),
      body: SafeArea(
        child: Column(
          children: [
            // Header Image area
            Expanded(
              flex: 2,
              child: Center(
                child: Container(
                  width: 250,
                  height: 80,
                  decoration: BoxDecoration(
                    color: const Color(0xCC81C784),
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: const Center(
                    child: Text(
                      'ratnagiri\nimpex',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF0D47A1),
                      ),
                    ),
                  ),
                ),
              ),
            ),
            // Form area
            Expanded(
              flex: 8,
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
                decoration: const BoxDecoration(
                  color: Color(0xFF558B2F), // Slightly different green based on image
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(50),
                  ),
                ),
                child: SingleChildScrollView(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'Sign Up 🌿',
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                      const SizedBox(height: 8),
                      const Text(
                        'Enter your details below',
                        style: TextStyle(fontSize: 16, color: Colors.white),
                      ),
                      const SizedBox(height: 20),
                      
                      _buildTextField('Select Type *', isDropdown: true),
                      const SizedBox(height: 12),
                      _buildTextField('Full Name *'),
                      const SizedBox(height: 12),
                      _buildTextField('Mobile Number'),
                      const SizedBox(height: 12),
                      _buildTextField('Email *'),
                      const SizedBox(height: 12),
                      _buildTextField('Password *', obscureText: true),
                      const SizedBox(height: 12),
                      _buildTextField('PAN Number'),
                      
                      const SizedBox(height: 16),
                      Row(
                        children: [
                          Checkbox(
                            value: _termsAccepted,
                            onChanged: (val) {
                              setState(() {
                                _termsAccepted = val ?? false;
                              });
                            },
                            fillColor: WidgetStateProperty.resolveWith(
                              (states) => Colors.yellow,
                            ),
                            checkColor: Colors.black,
                          ),
                          const Text(
                            'Terms and Conditions',
                            style: TextStyle(
                              color: Colors.white,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 16),
                      SizedBox(
                        width: 140,
                        child: ElevatedButton(
                          onPressed: () {
                            Navigator.pop(context); // Go back to login
                          },
                          style: ElevatedButton.styleFrom(
                            backgroundColor: const Color(0xFF00695C),
                            foregroundColor: Colors.white,
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8),
                            ),
                          ),
                          child: const Text('SIGN UP'),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTextField(String hint, {bool isDropdown = false, bool obscureText = false}) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(8),
      ),
      child: isDropdown
          ? DropdownButtonFormField<String>(
              decoration: const InputDecoration(
                contentPadding: EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                border: InputBorder.none,
              ),
              hint: Text(hint),
              items: const [],
              onChanged: (val) {},
            )
          : TextField(
              obscureText: obscureText,
              decoration: InputDecoration(
                hintText: hint,
                contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                border: InputBorder.none,
              ),
            ),
    );
  }
}
