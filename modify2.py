
import re

with open("frontend/src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update handleDetailsSubmit
old_details_submit = """  const handleDetailsSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!resumeFile) {
      setSubmitError("Please upload your resume.");
      return;
    }
    setSubmitError("");
    setStep("verification");
  };"""
new_details_submit = """  const handleDetailsSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitError("");
    setStep("legal");
  };"""
content = content.replace(old_details_submit, new_details_submit)

# 2. Update steps array
old_steps = """  const steps = [
    { id: "details", label: "Application Details" },
    { id: "verification", label: "Email Verification" },
    { id: "legal", label: "Legal Notice" },
  ];"""
new_steps = """  const steps = [
    { id: "details", label: "Application Details" },
    { id: "legal", label: "Legal Notice" },
  ];"""
content = content.replace(old_steps, new_steps)

# 3. Update stepOrder
content = content.replace(
    """const stepOrder = ["details", "verification", "legal"];""",
    """const stepOrder = ["details", "legal"];"""
)

# 4. Remove Email Verification UI Block
content = re.sub(r"\{\/\*\s*Step 2: Email Verification\s*\*\/\}[\s\S]*?(?=\{\/\*\s*Step 1: Application Form\s*\*\/\})", "", content)

# 5. Make fields optional
content = content.replace("<Field label=\"Full Name\">", "<Field label=\"Full Name\" optional>")
content = content.replace("type=\"text\" required placeholder=\"Your name\"", "type=\"text\" placeholder=\"Your name\"")

content = content.replace("<Field label=\"Location\">", "<Field label=\"Location\" optional>")
content = content.replace("type=\"text\" required placeholder=\"City, Country\"", "type=\"text\" placeholder=\"City, Country\"")

content = content.replace("<Field label=\"Phone Number\">", "<Field label=\"Phone Number\" optional>")
content = content.replace("type=\"tel\" required placeholder=\"+1 234 567 8900\"", "type=\"tel\" placeholder=\"+1 234 567 8900\"")

content = content.replace("<Field label=\"LinkedIn\">", "<Field label=\"LinkedIn\" optional>")
content = content.replace("type=\"url\" required placeholder=\"linkedin.com/in/yourname\"", "type=\"url\" placeholder=\"linkedin.com/in/yourname\"")

content = content.replace("<Field label=\"Resume\">", "<Field label=\"Resume\" optional>")

content = content.replace("<Field key={i} label={q}>", "<Field key={i} label={q} optional>")
content = content.replace("                        <textarea\\n                          required\\n                          rows={2}", "                        <textarea\\n                          rows={2}")
# alternative to above line using re
content = re.sub(r"<textarea\s+required", "<textarea", content)

# Update Email Field
old_email_field = """                  {/* Email Input */}
                  <Field label="Email Address">
                    <div className="flex flex-col gap-1">
                      <input type="email" required disabled={emailOtpVerified} placeholder="you@example.com" value={email} onChange={(e) => setEmail(e.target.value)}
                        className={fieldBase} style={fieldStyle} onFocus={focusField} onBlur={blurField} />
                      {emailOtpVerified ? (
                        <p className="text-xs text-green-600 font-semibold">
                          ? Verified
                        </p>
                      ) : (
                        <p className="text-xs" style={{ color: TEXT_MUTED }}>
                          <em>You will verify this email in the next step.</em>
                        </p>
                      )}
                    </div>
                  </Field>"""
new_email_field = """                  {/* Email Input */}
                  <Field label="Email Address" optional>
                    <input type="email" placeholder="you@example.com" value={email} onChange={(e) => setEmail(e.target.value)}
                      className={fieldBase} style={fieldStyle} onFocus={focusField} onBlur={blurField} />
                  </Field>"""
content = content.replace(old_email_field, new_email_field)

with open("frontend/src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

print("Modifications applied.")

