import SwiftUI

struct ContentView: View {
    @State private var helmet = false
    @State private var gloves = false
    @State private var boots = false
    @State private var incidentText = ""
    @Environment(\.openURL) private var openURL

    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Chequeo de EPIs")) {
                    Toggle("Casco", isOn: $helmet)
                    Toggle("Guantes", isOn: $gloves)
                    Toggle("Botas de seguridad", isOn: $boots)
                }
                Section(header: Text("Incidencias")) {
                    TextEditor(text: $incidentText)
                        .frame(height: 100)
                }
                Button("Enviar reporte") {
                    sendReport()
                }
            }
            .navigationTitle("Prevención")
        }
    }

    private func sendReport() {
        var body = "Casco: \(helmet ? \"Sí\" : \"No\")\n"
        body += "Guantes: \(gloves ? \"Sí\" : \"No\")\n"
        body += "Botas de seguridad: \(boots ? \"Sí\" : \"No\")\n\n"
        body += "Incidencias:\n\(incidentText)"

        let subject = "Chequeo EPIs"
        let address = "marlenwow@icloud.com"
        let urlString = "mailto:\(address)?subject=\(subject.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? "")&body=\(body.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? "")"
        if let url = URL(string: urlString) {
            openURL(url)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
