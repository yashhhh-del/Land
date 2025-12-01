import React, { useState } from 'react';
import { FileText, Sparkles, Edit2, Save, Copy, Check } from 'lucide-react';

export default function LandPropertyWriter() {
  const [formData, setFormData] = useState({
    propertyType: 'Residential Plot',
    location: '',
    area: '',
    unit: 'sq ft',
    price: '',
    facing: 'East',
    roadWidth: '',
    surroundings: '',
    amenities: '',
    legalStatus: 'Clear Title',
    additionalInfo: ''
  });

  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [isEditing, setIsEditing] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const generateDescription = async () => {
    setLoading(true);
    setError('');
    
    const prompt = `Write a professional and attractive property description for a land listing based on the following details:

Property Type: ${formData.propertyType}
Location: ${formData.location}
Area: ${formData.area} ${formData.unit}
Price: ${formData.price}
Facing: ${formData.facing}
Road Width: ${formData.roadWidth}
Surroundings: ${formData.surroundings}
Amenities: ${formData.amenities}
Legal Status: ${formData.legalStatus}
Additional Information: ${formData.additionalInfo}

Write a compelling description that highlights the key features, location advantages, and investment potential. Keep it professional, engaging, and around 150-200 words.`;

    try {
      const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer YOUR_GROQ_API_KEY_HERE'
        },
        body: JSON.stringify({
          model: 'llama-3.3-70b-versatile',
          messages: [
            {
              role: 'user',
              content: prompt
            }
          ],
          temperature: 0.7,
          max_tokens: 500
        })
      });

      if (!response.ok) {
        throw new Error('Failed to generate description. Please check your API key.');
      }

      const data = await response.json();
      setDescription(data.choices[0].message.content);
      setIsEditing(false);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(description);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-6xl mx-auto">
        <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-6 text-white">
            <div className="flex items-center gap-3">
              <FileText className="w-8 h-8" />
              <div>
                <h1 className="text-3xl font-bold">AI Property Description Writer</h1>
                <p className="text-blue-100 mt-1">Generate professional land property descriptions instantly</p>
              </div>
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-6 p-6">
            {/* Form Section */}
            <div className="space-y-4">
              <h2 className="text-xl font-bold text-gray-800 mb-4">Property Details</h2>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Property Type</label>
                <select
                  name="propertyType"
                  value={formData.propertyType}
                  onChange={handleInputChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option>Residential Plot</option>
                  <option>Commercial Plot</option>
                  <option>Agricultural Land</option>
                  <option>Industrial Plot</option>
                  <option>Farm Land</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Location *</label>
                <input
                  type="text"
                  name="location"
                  value={formData.location}
                  onChange={handleInputChange}
                  placeholder="e.g., Near Highway, City Center"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Area *</label>
                  <input
                    type="text"
                    name="area"
                    value={formData.area}
                    onChange={handleInputChange}
                    placeholder="1000"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Unit</label>
                  <select
                    name="unit"
                    value={formData.unit}
                    onChange={handleInputChange}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option>sq ft</option>
                    <option>sq yards</option>
                    <option>acres</option>
                    <option>hectares</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Price</label>
                <input
                  type="text"
                  name="price"
                  value={formData.price}
                  onChange={handleInputChange}
                  placeholder="e.g., ₹50 Lakhs"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Facing</label>
                  <select
                    name="facing"
                    value={formData.facing}
                    onChange={handleInputChange}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option>East</option>
                    <option>West</option>
                    <option>North</option>
                    <option>South</option>
                    <option>North-East</option>
                    <option>South-East</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Road Width</label>
                  <input
                    type="text"
                    name="roadWidth"
                    value={formData.roadWidth}
                    onChange={handleInputChange}
                    placeholder="e.g., 40 ft"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Surroundings</label>
                <input
                  type="text"
                  name="surroundings"
                  value={formData.surroundings}
                  onChange={handleInputChange}
                  placeholder="Schools, hospitals, markets nearby"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Amenities</label>
                <input
                  type="text"
                  name="amenities"
                  value={formData.amenities}
                  onChange={handleInputChange}
                  placeholder="Water, electricity, drainage"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Legal Status</label>
                <select
                  name="legalStatus"
                  value={formData.legalStatus}
                  onChange={handleInputChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option>Clear Title</option>
                  <option>Approved Layout</option>
                  <option>RERA Approved</option>
                  <option>Freehold</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Additional Information</label>
                <textarea
                  name="additionalInfo"
                  value={formData.additionalInfo}
                  onChange={handleInputChange}
                  placeholder="Any other details..."
                  rows="3"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              <button
                onClick={generateDescription}
                disabled={loading || !formData.location || !formData.area}
                className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3 rounded-lg font-semibold hover:from-blue-700 hover:to-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 transition-all"
              >
                {loading ? (
                  <>
                    <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                    Generating...
                  </>
                ) : (
                  <>
                    <Sparkles className="w-5 h-5" />
                    Generate Description
                  </>
                )}
              </button>
            </div>

            {/* Description Section */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-bold text-gray-800">Generated Description</h2>
                {description && (
                  <div className="flex gap-2">
                    <button
                      onClick={() => setIsEditing(!isEditing)}
                      className="px-3 py-2 text-sm bg-gray-100 hover:bg-gray-200 rounded-lg flex items-center gap-2 transition-colors"
                    >
                      {isEditing ? <Save className="w-4 h-4" /> : <Edit2 className="w-4 h-4" />}
                      {isEditing ? 'Save' : 'Edit'}
                    </button>
                    <button
                      onClick={copyToClipboard}
                      className="px-3 py-2 text-sm bg-green-100 hover:bg-green-200 text-green-700 rounded-lg flex items-center gap-2 transition-colors"
                    >
                      {copied ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
                      {copied ? 'Copied!' : 'Copy'}
                    </button>
                  </div>
                )}
              </div>

              <div className="bg-gray-50 rounded-lg p-6 min-h-[400px] border-2 border-gray-200">
                {error && (
                  <div className="bg-red-50 border border-red-200 text-red-700 p-4 rounded-lg mb-4">
                    <p className="font-medium">Error:</p>
                    <p className="text-sm">{error}</p>
                    <p className="text-xs mt-2">Please replace 'YOUR_GROQ_API_KEY_HERE' with your actual Groq API key in the code.</p>
                  </div>
                )}
                
                {!description && !error && (
                  <div className="flex flex-col items-center justify-center h-full text-gray-400">
                    <FileText className="w-16 h-16 mb-4" />
                    <p className="text-center">Fill in the property details and click<br/>"Generate Description" to create your listing</p>
                  </div>
                )}

                {description && (
                  isEditing ? (
                    <textarea
                      value={description}
                      onChange={(e) => setDescription(e.target.value)}
                      className="w-full h-full min-h-[350px] p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                    />
                  ) : (
                    <div className="prose prose-sm max-w-none">
                      <p className="whitespace-pre-wrap text-gray-700 leading-relaxed">{description}</p>
                    </div>
                  )
                )}
              </div>

              {description && (
                <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                  <p className="text-sm text-blue-800">
                    <strong>Tip:</strong> You can edit the generated description by clicking the "Edit" button above. The description is fully customizable to match your needs.
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Setup Instructions */}
          <div className="bg-yellow-50 border-t border-yellow-200 p-4">
            <p className="text-sm text-yellow-800">
              <strong>Setup Required:</strong> Replace <code className="bg-yellow-100 px-2 py-1 rounded">YOUR_GROQ_API_KEY_HERE</code> in the code with your free Groq API key. 
              Get yours at <a href="https://console.groq.com" target="_blank" rel="noopener noreferrer" className="underline font-medium">console.groq.com</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
