import SwiftUI

struct ContentView: View {
    @State private var number1: String = ""
    @State private var number2: String = ""
    @State private var result: String = "0"

    var body: some View {
        VStack {
            Text("Kalkulator Sederhana")
                .font(.largeTitle)
                .padding()

            TextField("Angka pertama", text: $number1)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
                .keyboardType(.decimalPad)

            TextField("Angka kedua", text: $number2)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
                .keyboardType(.decimalPad)

            HStack {
                Button(action: { calculate("+") }) {
                    Text("+")
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }
                Button(action: { calculate("-") }) {
                    Text("-")
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.red)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }
            }
            .padding()

            Text("Hasil: